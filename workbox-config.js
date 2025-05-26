module.exports = {
	globDirectory: '.',
	globPatterns: [
		'**/*.{css,png,MID,wav,html,js,wasm,json,md,zip,py,cmd,txt,vai,dat,pas}'
	],
	swDest: 'sw.js',
	ignoreURLParametersMatching: [
		/^utm_/,
		/^fbclid$/
	]
};