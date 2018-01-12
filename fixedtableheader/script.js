// jshint esversion: 6, browser: true, devel: true
const thElements = document.getElementsByTagName( 'th' ),
	tdElements = document.getElementsByTagName( 'td' );
for ( let i = 0; i < thElements.length; i++ ) {
	const widerElement = thElements[ i ].offsetWidth > tdElements[ i ].offsetWidth ? thElements[ i ] : tdElements[ i ],
		width = window.getComputedStyle( widerElement ).width;
	thElements[ i ].style.width = tdElements[ i ].style.width = width;
}
