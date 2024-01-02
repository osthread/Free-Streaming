document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
}, false);

document.addEventListener('keydown', function(e) {
    if (e.key === 'F12' || (e.ctrlKey && e.shiftKey && (e.key === 'I' || e.key === 'C' || e.key === 'J'))) {
        e.preventDefault();
    }
}, false);

(function() {
    var devToolsOpen = false;
    var threshold = 160;

    function detectDevTool(allow) {
        if (!allow) {
            window.location.href = '/';
        }
    }

    setInterval(function() {
        var widthThreshold = window.outerWidth - window.innerWidth > threshold;
        var heightThreshold = window.outerHeight - window.innerHeight > threshold;
        var orientation = widthThreshold ? 'vertical' : 'horizontal';

        if (!(heightThreshold && widthThreshold) &&
            ((window.Firebug && window.Firebug.chrome && window.Firebug.chrome.isInitialized) || widthThreshold || heightThreshold)) {
            if (!devToolsOpen || orientation !== devToolsOrientation) {
                devToolsOpen = true;
                devToolsOrientation = orientation;
                detectDevTool(false);
            }
        } else {
            if (devToolsOpen) {
                devToolsOpen = false;
                devToolsOrientation = undefined;
                detectDevTool(true);
            }
        }
    }, 500);

    if (typeof module !== 'undefined' && module.exports) {
        module.exports = detectDevTool;
    }
    window.detectDevTool = detectDevTool;
})();