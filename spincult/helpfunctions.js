/*exported distFromLine*/
// returns distance of point p to line segment x, y,xx,yy
let distFromLine = function (px, py, x, y, xx, yy) {

	let vx = xx - x,
		vy = yy - y,
		pvx = px - x,
		pvy = py - y,
		u = (pvx * vx + pvy * vy) / (vy * vy + vx * vx);

	if (u >= 0 && u <= 1) {
		let lx = vx * u,
			ly = vy * u;

		return Math.sqrt(Math.pow(ly - pvy, 2) + Math.pow(lx - pvx, 2));
	}

	// closest point past ends of line so get dist to closest end
	return Math.min(Math.sqrt(Math.pow(xx - px, 2) + Math.pow(yy - py, 2)), Math.sqrt(Math.pow(x - px, 2) + Math.pow(y - py, 2)));
};
