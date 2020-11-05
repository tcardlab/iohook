{
  "variables": {
    'v8_enable_pointer_compression': 1
  },
	"targets": [{
		"target_name": "uiohook",
		"type": "shared_library",
		"sources": [
			"libuiohook/include/uiohook.h",
			"libuiohook/src/logger.c",
			"libuiohook/src/logger.h",
			"libuiohook/src/darwin/input_helper.h",
			"libuiohook/src/darwin/input_helper.c",
			"libuiohook/src/darwin/input_hook.c",
			"libuiohook/src/darwin/post_event.c",
			"libuiohook/src/darwin/system_properties.c"
		],
		"include_dirs": [
			'node_modules/nan',
			'libuiohook/include',
			'libuiohook/src'
		]
	}]
}
