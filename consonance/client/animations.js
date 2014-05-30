state="out";
fadeLoop = null;
slideLoop = null;
sLeft = true;

function fadeLyrics() {
    if (state=="in"){
        state = "out";
        $("#lyrics_container").fadeIn(1000);
    } else if (state=="out"){
        state = "in";
        $("#lyrics_container").fadeOut(1000);
    }
}

function startFadingLyrics(){
    fadeLoop = setInterval(fadeLyrics,1000);
}

function stopFadingLyrics(){
    clearInterval(fadeLoop);
}

function slideAnimation(){
    if (sLeft){
        $("#lyrics_hr_top").animate({"margin-left" : "-20%",}, 500);
        $("#lyrics_hr_bot").animate({"margin-right" : "-20%",}, 500);
        sLeft = false;
    }
    else {
        $("#lyrics_hr_top").animate({"margin-left" : "0%",}, 500);
        $("#lyrics_hr_bot").animate({"margin-right" : "0%",}, 500);
        sLeft = true;
    }
}

function startSlideAnimation(){
    slideLoop = setInterval(slideAnimation,1000);
}