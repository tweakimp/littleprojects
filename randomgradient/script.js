/* jshint esversion: 6, browser: true, devel: true */
const settings = {
	width: 900,
	height: 300,
	minColorValue: 70,
	maxColorValue: 185,
	header: {
		text: "style",
		font: "calibri",
		weight: "bolder",
		size: "150px",
		offset: 7,
	}
};
let container = document.getElementsByClassName( "container" )[ 0 ];
let firstColor = [ 0, 0, 0 ];
let secondColor = [ 0, 0, 0 ];
let create = function( width, height ) {
	let canvas = document.createElement( "canvas" );
	canvas.width = width;
	canvas.height = height;
	container.appendChild( canvas );
};
let colorPicker = function() {
	let configurations = [
		[ 0, 1, 2 ],
		[ 0, 2, 1 ],
		[ 1, 0, 2 ],
		[ 1, 2, 0 ],
		[ 2, 0, 1 ],
		[ 2, 1, 0 ],
	];
	let randomConfig = configurations[ random( 0, 5 ) ];
	firstColor[ randomConfig[ 0 ] ] = settings.minColorValue;
	firstColor[ randomConfig[ 1 ] ] = settings.maxColorValue;
	firstColor[ randomConfig[ 2 ] ] = random( settings.minColorValue, settings.maxColorValue );
	let shiftAmount = random( 1, 2 );
	let secondConfig = [ 0, 0, 0 ];
	for ( let i = 0; i < 3; i++ ) {
		if ( i + shiftAmount < 3 ) {
			secondConfig[ i ] = randomConfig[ i + shiftAmount ];
		} else {
			secondConfig[ i ] = randomConfig[ i - 3 + shiftAmount ];
		}
	}
	secondColor[ secondConfig[ 0 ] ] = settings.minColorValue;
	secondColor[ secondConfig[ 1 ] ] = settings.maxColorValue;
	secondColor[ secondConfig[ 2 ] ] = random( settings.minColorValue, settings.maxColorValue );
};
let fill = function() {
	let canvas = document.getElementsByTagName( "canvas" )[ 0 ];
	let context = canvas.getContext( "2d" );
	let gradient = context.createLinearGradient( 0, 0, settings.width, settings.height );
	gradient.addColorStop( 0, `rgb(${firstColor[0]},${firstColor[1]},${firstColor[2]})` );
	gradient.addColorStop( 1, `rgb(${secondColor[0]},${secondColor[1]},${secondColor[2]})` );
	context.fillStyle = gradient;
	context.fillRect( 0, 0, settings.width, settings.height );
};
let printText = function() {
	let canvas = document.getElementsByTagName( "canvas" )[ 0 ];
	let context = canvas.getContext( "2d" );
	context.font = `${settings.header.weight} ${settings.header.size} ${settings.header.font}`;
	context.fillStyle = "rgba(255, 255, 255, 0.5)";
	context.textAlign = "center";
	context.textBaseline = "middle";
	context.fillText( settings.header.text, settings.width / 2, settings.height / 2 );
	context.fillText( settings.header.text, settings.header.offset + settings.width / 2, settings.height / 2 );
	context.fillText( settings.header.text, -settings.header.offset + settings.width / 2, settings.height / 2 );
};
let start = function() {
	create( settings.width, settings.height );
	colorPicker();
	fill();
	printText();
};
// help function
function random( min, max ) {
	return Math.floor( Math.random() * ( max - min + 1 ) ) + min;
}
