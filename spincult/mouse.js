/*exported mouseInOutCallback, createMouse*/
const MOUSE = {
	buttonMasks: [1, 2, 4, 6, 5, 3],

	// contextmenu is included as that needs to be blocked for right button events
	events: ["mousemove", "mousedown", "mouseup", "mouseout", "mouseover", "contextmenu"]
};

// fix m, t letiables: no one letter names
function mouseEvent(e) {

	// lazy programer short cut
	let m = this,
		t = e.type,
		bounds = m.element.getBoundingClientRect();
	m.x = e.clientX - bounds.left;
	m.y = e.clientY - bounds.top;
	if (t === "mousedown") {
		m.button |= MOUSE.buttonMasks[e.which - 1];
	} else if (t === "mouseup") {
		m.button &= MOUSE.buttonMasks[e.which + 2];
	} else if (t === "mouseout") {
		m.button = 0;
		m.over = false;
		m.table.mouseOver();
	} else if (t === "mouseover") {
		m.over = true;
		m.table.mouseOver();
	}
	e.preventDefault();
}

// mousecallback starts a table rendering if not already doing so
function mouseInOutCallback() {
	if (this.mouse.over) {
		if (!this.updating) {
			this.update();
		}
	} else {
		this.div.style.cursor = "default";
	}
}

// create the mouse inteface for a table
function createMouse(table) {
	let mouse = {
		x: 0,
		y: 0,
		over: false,
		table: table,
		element: table.div,
		button: 0
	};
	mouse.event = mouseEvent.bind(mouse);
	mouse.start = function () {
		MOUSE.events.forEach(n => {
			this.element.addEventListener(n, this.event);
		});
	};
	mouse.remove = function () {
		MOUSE.events.forEach(n => {
			this.element.removeEventListener(n, this.event);
		});
	};
	return mouse;
}
