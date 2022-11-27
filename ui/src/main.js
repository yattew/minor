
const electron = require('electron');
// Module to control application life.
const app = electron.app;
// Module to create native browser window.
const BrowserWindow = electron.BrowserWindow;

const path = require('path');
const url = require('url');
var spawn = require("child_process").spawn;
const child = spawn('python', ['./../scripts/api.py'])
// use if you want text chunks
child.stdout.setEncoding('utf8');
child.stdout.on('data', (chunk) => {
    console.log(chunk);
    if (chunk.length >= 3) {
        let [u, url, _] = chunk.split(" ");
        console.log("url is: ", url);
        if (u == "url") {
            mainWindow.loadURL(url);
        }
    }
});
child.stderr.setEncoding('utf8');
child.stderr.on('data', (chunk) => {
    console.log(chunk);
});

// since these are streams, you can pipe them elsewhere
//child.stderr.pipe(dest);

child.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
});

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
const contextMenu = require('electron-context-menu');

contextMenu({
    showSaveImageAs: true
});
let mainWindow;
module.exports = {
    win: mainWindow
}

function createWindow() {

    // Create the browser window.
    mainWindow = new BrowserWindow({ width: 1920, height: 1080 });
    // and load the index.html of the app.
    mainWindow.loadURL('http://localhost:3000');
    mainWindow.removeMenu();

    // Open the DevTools.
    //mainWindow.webContents.openDevTools();

    // Emitted when the window is closed.
    mainWindow.on('closed', function () {
        // Dereference the window object, usually you would store windows
        // in an array if your app supports multi windows, this is the time
        // when you should delete the corresponding element.
        mainWindow = null
    })
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow);

// Quit when all windows are closed.
app.on('window-all-closed', function () {
    // On OS X it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== 'darwin') {
        app.quit()
    }
});

app.on('activate', function () {
    // On OS X it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (mainWindow === null) {
        createWindow()
    }
});




const http = require('http');
const windows = new Set();
const requestListener = function (req, res) {
    const contextMenu = require('electron-context-menu');
    contextMenu({
        showSaveImageAs: true
    });
    let q = url.parse(req.url, true).query;
    let re_url = q.url;
    console.log("redirecting to: ", re_url);
    let newWindow = new BrowserWindow();

    newWindow.loadURL(re_url);
    function onClosed() {
        windows.delete(newWindow);
        newWindow.removeAllListeners();
        newWindow = null;
    }
    newWindow.on('closed', onClosed);

    windows.add(newWindow);
    const headers = {
        'Access-Control-Allow-Origin': '*', /* @dev First, read about security */
        'Access-Control-Allow-Methods': 'OPTIONS, POST, GET',
        'Access-Control-Max-Age': 2592000,
    };
    res.writeHead(200, headers);
    res.end('asdf');
}

const server = http.createServer(requestListener);
server.listen(8080);
// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.