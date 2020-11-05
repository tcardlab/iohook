{
  "variables": {
    'v8_enable_pointer_compression': 1
  },
	"targets": [{
		"target_name": "iohook",
		"win_delay_load_hook": "true",
		"type": "shared_library",
		"sources": [
			"src/iohook.cc",
			"src/iohook.h"
		],
		"dependencies": [
			"./uiohook.gyp:uiohook"
		],
		"include_dirs": [
			"<!(node -e \"require('nan')\")",
			"libuiohook/include"
		],
		"configurations": {
			"Release": {
			}
		}
	}]
}
