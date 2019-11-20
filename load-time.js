// from https://timkadlec.com/me/
window.onload = function(){
  setTimeout(function(){
    window.performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {};
    var t = performance.timing || {};

    if (!t) {

      return;
    }
    var start = t.navigationStart,
        end = t.loadEventEnd
        loadTime = (end - start) / 1000;

    var copy = document.querySelectorAll('.copy');
    copy[0].innerHTML += "<p class='loaded'>This page loaded in <strong>" + loadTime + " seconds</strong>.</p>";
  }, 0); 
}
