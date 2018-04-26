cordova.define('cordova/plugin_list', function(require, exports, module) {
module.exports = [
    {
        "file": "plugins/com.tlantic.plugins.socket/www/socket.js",
        "id": "com.tlantic.plugins.socket.Socket",
        "pluginId": "com.tlantic.plugins.socket",
        "clobbers": [
            "window.tlantic.plugins.socket"
        ]
    }
];
module.exports.metadata = 
// TOP OF METADATA
{
    "com.tlantic.plugins.socket": "0.3.0",
    "cordova-plugin-websocket": "0.12.2"
}
// BOTTOM OF METADATA
});