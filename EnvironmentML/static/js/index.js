function fadeInPage() {
    var $this = $(this);
    if ($this.scrollTop() >= 10) {
        $(".navbar").addClass("scrolled");
    } else {
        $(".navbar").removeClass("scrolled");
    }
    if (!window.AnimationEvent) {
        return;
    }
    var fader = document.getElementById('page-fader');
    fader.classList.add('fade-out');

}

document.addEventListener('DOMContentLoaded', function () {
    if (!window.AnimationEvent) {
        return;
    }
    var anchors = document.getElementsByTagName('a');

    for (var idx = 0; idx < anchors.length; idx += 1) {
        if (anchors[idx].hostname !== window.location.hostname ||
            anchors[idx].pathname === window.location.pathname) {
            continue;
        }
        anchors[idx].addEventListener('click', function (event) {
            var fader = document.getElementById('page-fader'),
                anchor = event.currentTarget;

            var listener = function () {
                window.location = anchor.href;
                fader.removeEventListener('animationend', listener);
            };
            fader.addEventListener('animationend', listener);

            event.preventDefault();
            fader.classList.add('fade-in');
        });
    }
});
window.addEventListener('pageshow', function (event) {
    if (!event.persisted) {
        return;
    }
    var fader = document.getElementById('page-fader');
    fader.classList.remove('fade-in');
});


$(window).scroll(function () {
    var $this = $(this);
    if ($this.scrollTop() >= 10) {
        $(".navbar").addClass("scrolled");
    } else {
        $(".navbar").removeClass("scrolled");
    }
});

