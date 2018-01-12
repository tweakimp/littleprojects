/*globals mouseInOutCallback, createMouse, distFromLine*/
let tableArray = [];

const globalScale = 1;
const shadow = "rgba(0,0,0,0.75)";
const white = "white";
const tableRefreshDelay = 50;

const TABLE = {

	width: 223 * globalScale,
	height: 314 * globalScale,
	tables: document.getElementById("tables"),
	image: {
		shadow: shadow,
		shadowBlur: 20 * globalScale,
		area: "#2e3f73",
		lines: "#ffffff",
		lineWidth: 8 * globalScale,
		cursor: "default"
	},
	empty: {
		inset: 30 * globalScale,
		lines: "rgba(255,255,255,0.5)",
		lineWidth: 8 * globalScale,
		shadow: shadow,
		shadowBlur: 20 * globalScale,
		cursor: "pointer",
		highlightAmount: 0.6
	},
	arrow: {
		width: 5 * globalScale,
		shadow: shadow,
		shadowBlur: 5 * globalScale,
		fill: "#ffb900",
		highlight: "#ffdc44",
		lineWidth: 1,
		line: "#ffdc44",
		lineHigh: "#ffed55",
		head: 15 * globalScale,

		// min size arrow can be, if smaller then arrow is not created
		minSize: 5
	},

	// dom settings for table canvas and div tags
	DOM: {
		display: "inline-block",
		canvasClass: "table",
		zIndex: 1
	},

	// styles for rendering and display close icon
	closeIcon: {
		size: 32 * globalScale,
		fill: "red",
		lines: white,
		lineWidth: Math.max(1, 2 * globalScale),
		shadow: shadow,
		shadowBlur: 5 * globalScale,
		cursor: "pointer",
		pos: {
			// as fractions
			x: 1,
			y: 0
		}
	}
};

// set up functions create images and do other general setup
// sets common context settings
function setupContext(context, descript) {
	context.shadowBlur = descript.shadowBlur;
	context.shadowColor = descript.shadow;
	context.strokeStyle = descript.lines;
	context.fillStyle = descript.fill;
	context.lineWidth = descript.lineWidth;
	context.lineCap = "round";
	if (descript.font) {
		context.font = descript.font.size + descript.font.face;
	}
}

function createTableImage() {
	let table = document.createElement("canvas"),
		context = table.getContext("2d"),
		scaleX = TABLE.width / 223,
		scaleY = TABLE.height / 314;
	table.height = TABLE.height;
	setupContext(context, TABLE.image);

	// apply shadow to area and net
	context.save();
	context.shadowBlur = 10;
	context.shadowColor = shadow;
	context.fillStyle = TABLE.image.area;
	context.fillRect(35.25, 20, 152.5, 274);

	// net color
	context.fillStyle = TABLE.image.lines;

	// net
	context.fillRect(20, 156, 183, 2);

	// dont apply to lines
	context.restore();

	// lines
	context.fillStyle = TABLE.image.lines;
	context.fillRect(111.35, 20, 0.3, 274);
	context.fillRect(35.25, 20, 2, 274);
	context.fillRect(185.75, 20, 2, 274);
	context.fillRect(35.25, 20, 152.5, 2);
	context.fillRect(35.25, 292, 152.5, 2);
	return table;
}

function createEmptyImage() {
	let i = TABLE.empty.inset,
		image = document.createElement("canvas"),
		w = image.width = TABLE.width,
		h = image.height = TABLE.height,
		context = image.getContext("2d");
	setupContext(context, TABLE.empty);
	context.lineWidth = 7;
	context.strokeRect(i, i, w - i * 2, h - i * 2);
	context.beginPath();

	// horizontal line
	context.moveTo(w / 2 - 2 * i, h / 2);
	context.lineTo(w / 2 + 2 * i, h / 2);

	// vertical line
	context.moveTo(w / 2, h / 2 - 2 * i);
	context.lineTo(w / 2, h / 2 + 2 * i);
	context.stroke();
	return image;
}

function createCloseImage() {
	let S = TABLE.closeIcon.size,
		s = S * 0.5,

		// cross dist from center
		c = s * 0.4,
		sb = TABLE.closeIcon.shadowBlur,
		l = TABLE.closeIcon.lineWidth,
		image = document.createElement("canvas"),

		// add half blur to get center
		cx = s + sb / 2,
		cy = s + sb / 2,
		context = image.getContext("2d");

	// image must include shadowblur
	// add blur to size
	image.width = S + sb;
	image.height = S + sb;
	setupContext(context, TABLE.closeIcon);
	context.beginPath();
	context.arc(cx, cy, s - l, 0, Math.PI * 2);
	context.fill();
	context.stroke();
	context.beginPath();
	context.moveTo(cx - c, cy - c);
	context.lineTo(cx + c, cy + c);
	context.moveTo(cx - c, cy + c);
	context.lineTo(cx + c, cy - c);
	context.stroke();
	return image;
}

// create the images
// draws an arrow, a is the arrow object
function drawArrow(context, a) {

	// get arrow style
	let s = TABLE.arrow,
		x = a.x,
		y = a.y,
		vx = a.xx - x,
		vy = a.yy - y,
		dir = Math.atan2(vy, vx),
		len = Math.sqrt(vx * vx + vy * vy),
		w = s.width / 2,

		// ensure arrow head no bigger than arrow length
		h = Math.min(len, s.head);
	// context.save();
	context.setTransform(1, 0, 0, 1, x, y);
	context.rotate(dir);
	h /= 2;
	if (a.highlight) {
		context.fillStyle = s.highlight;
		context.strokeStyle = s.lineHigh;
	} else {
		context.fillStyle = s.fill;
		context.strokeStyle = s.line;
	}
	context.lineWidth = s.lineWidth;
	context.save();
	context.shadowBlur = s.shadowBlur;
	context.shadowColor = s.shadow;
	context.beginPath();
	context.moveTo(0, -w / 2);
	context.lineTo(len - h - h, -w);
	context.lineTo(len - h - h, -h);
	context.lineTo(len, 0);
	context.lineTo(len - h - h, h);
	context.lineTo(len - h - h, w);
	context.lineTo(0, w / 2);
	context.closePath();
	context.fill();
	context.stroke();
	context.restore();
}

function drawClose() {
	let context = this.context,
		w = closeIcon.width,
		grow = w * 0.1,
		x = (this.width - w) * TABLE.closeIcon.pos.x,
		y = (this.height - w) * TABLE.closeIcon.pos.y,

		// icon x and y
		icX = x + w / 2,
		icY = y + w / 2,
		dist = Math.sqrt(Math.pow(this.mouse.x - icX, 2) + Math.pow(this.mouse.y - icY, 2));
	if (dist < TABLE.closeIcon.size / 2) {
		this.mouseOverClose = true;
	} else {
		this.mouseOverClose = false;
	}
	context.globalAlpha = 1 - (Math.min(100, (dist - w * 2)) / 100);
	if (this.mouseOverClose) {
		context.drawImage(closeIcon, x - grow, y - grow, w + grow * 2, w + grow * 2);
	} else {
		context.drawImage(closeIcon, x, y);
	}
	context.globalAlpha = 1;
}



function removeTable(table) {

	// deactivate mouse events
	table.mouse.remove();

	// remove from DOM
	TABLE.tables.removeChild(table.div);

	// flag as dead to be removed from table array
	table.dead = true;
}

function updateTables() {
	let closeTables = [];
	closeTables = tableArray.filter(function (t) {
		return !t.active;
	});
	while (closeTables.length > 1) {
		removeTable(closeTables.shift());
	}
	tableArray = tableArray.filter(function (cur) {
		return !cur.dead;
	});
}
let tableImage = createTableImage();
let closeIcon = createCloseImage();
let emptyTableImage = createEmptyImage();

function drawTable() {
	let context = this.context,

		// this sets the max distance mouse can be for it to highlight an arrow
		minDist = TABLE.arrow.width,
		dist = 0;
	context.clearRect(0, 0, context.canvas.width, context.canvas.height);
	if (this.active) {
		context.drawImage(tableImage, 0, 0);
		if (this.mouse.over) {

			// dont draw close icon while dragging
			if (!this.dragging) {
				this.drawCloseIcon();
			}
			// if not dragging and mouse over close
			if (this.mouseOverClose && !this.dragging) {

				// set cursor
				this.cursor = TABLE.closeIcon.cursor;

				// bit field if mouse left down
				if (this.mouse.button === 1) {
					this.buttonDown = true;

					// only close if mouse moves up while over close
				} else if (this.buttonDown) {
					this.active = false;
					this.buttonDown = false;
					setTimeout(updateTables, tableRefreshDelay);
				}
				// not over close
			} else {

				// if near a arrow and mouse button right is down delete the arrow
				// but field only button right down
				if (this.closestArrowIndex > -1 && this.mouse.button === 4) {
					this.arrows.splice(this.closestArrowIndex, 1);
					this.closestArrowIndex = -1;

					// turn mouse click off
					this.mouse.button = 0;
					// bit field if down start dragging new arrow
				} else if (this.mouse.button === 1) {
					// start of drag create arrow
					if (!this.dragging) {
						this.arrows.push({
							x: this.mouse.x,
							y: this.mouse.y,
							xx: this.mouse.x,
							yy: this.mouse.y
						});
						this.currentArrow = this.arrows[this.arrows.length - 1];
						this.dragging = true;

						// during drag move arrow endpoint
					} else {
						this.currentArrow.xx = this.mouse.x;
						this.currentArrow.yy = this.mouse.y;
					}

					// mouse up
				} else {

					// is dragging then must be a arrow
					if (this.dragging) {
						// if arrow added is smaller than 2 pixels then remove it;
						if (Math.abs(this.currentArrow.xx - this.currentArrow.x) < TABLE.arrow.minSize &&
							Math.abs(this.currentArrow.y - this.currentArrow.yy) < TABLE.arrow.minSize
						) {
							this.arrows.length -= 1;
						}
						this.currentArrow = null;
						this.dragging = false;
					}
				}

				// set cursor tp table standard
				this.cursor = TABLE.image.cursor;
			}
		}

		// is mouse near arrow
		if (this.closestArrowIndex > -1 && !this.dragging) {

			// yes set cursor for arrow
			this.cursor = TABLE.arrow.cursor;
		}
		this.closestArrowIndex = -1;

		// test all arrow
		for (let i = 0; i < this.arrows.length; i++) {
			let a = this.arrows[i];

			// draw the arrow
			drawArrow(context, a);
			a.highlight = false;
			dist = distFromLine(this.mouse.x, this.mouse.y, a.x, a.y, a.xx, a.yy);
			if (dist < minDist) {

				// yes remember the index
				this.closestArrowIndex = i;
				minDist = dist;
			}
		}

		// is an arrow close to mouse
		if (this.closestArrowIndex > -1 && this.mouse.over) {

			// highlight it
			this.arrows[this.closestArrowIndex].highlight = true;
		}

		// reset transform after arrows drawn
		context.setTransform(1, 0, 0, 1, 0, 0);
	} else {
		this.drawEmpty();
	}
}

// renders a table. stops rendering if the mouse is not over
function tableUpdate() {
	if (this.mouse.over) {
		this.updating = true;
		requestAnimationFrame(this.update);
	} else {

		// turn off button if dragged off
		this.buttonDown = false;
		this.div.style.cursor = "default";
		this.updating = false;

		// draw another time. This allows for the visual state to be correct
		this.draw();
	}
	this.draw();
	this.div.style.cursor = this.cursor;
}



function drawEmpty() {
	let context = this.context;
	context.drawImage(emptyTableImage, 0, 0);
	context.drawImage(emptyTableImage, 0, 0);
	if (this.mouse.over) {
		context.globalCompositeOperation = "lighter";
		context.globalAlpha = TABLE.empty.highlightAmount;
		context.drawImage(emptyTableImage, 0, 0);
		context.globalAlpha = 1;
		context.globalCompositeOperation = "source-over";
		this.cursor = TABLE.empty.cursor;

		// bit field
		if (this.mouse.button === 1) {
			this.buttonDown = true;
		} else if (this.buttonDown) {
			this.active = true;
			setTimeout(addTable, tableRefreshDelay);
			this.buttonDown = false;
		}
	} else {
		this.cursor = "default";
	}
}



function createAddTable() {
	let table = {},
		div = document.createElement("div"),
		canvas = document.createElement("canvas");
	div.style.width = TABLE.width + "px";
	div.style.height = TABLE.height + "px";
	div.style.display = TABLE.DOM.display;
	div.className = "table";
	canvas.width = TABLE.width;
	canvas.height = TABLE.height;
	canvas.className = TABLE.DOM.tableClass;
	canvas.style.zIndex = TABLE.DOM.zIndex;
	table.div = div;
	table.canvas = canvas;
	table.context = canvas.getContext("2d");
	table.arrows = [];
	table.width = TABLE.width;
	table.height = TABLE.height;
	table.mouseOverClose = false;
	table.drawCloseIcon = drawClose;
	table.draw = drawTable;
	table.dragging = false;
	table.active = false;
	table.update = tableUpdate.bind(table);

	// called by mouseEvent when mouse over out
	table.mouseOver = mouseInOutCallback;
	table.drawEmpty = drawEmpty.bind(table);

	// when removed and not needed it is dead and can then be removed from table array
	table.dead = false;

	// true if animation requests are happening
	table.updating = false;

	div.appendChild(canvas);
	table.mouse = createMouse(table);
	table.draw();
	return table;
}

// Adds a table to table array and DOM
function addTable() {

	// create new table
	let table = createAddTable();

	// add to the dom
	TABLE.tables.appendChild(table.div);

	// start the mouse
	table.mouse.start();

	// add to table array
	tableArray.push(table);
	return table;
}
addTable();
