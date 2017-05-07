var playlist = document.getElementsByClassName('track');
var music; //= playlist[0].getElementsByTagName('audio')[0];
var pButton = document.getElementById('pButton');
var playhead = document.getElementById('playhead');
var timeline = document.getElementById('timeline');
var timelineWidth = timeline.offsetWidth - playhead.offsetWidth;
var onplayhead = false;
var predict = document.getElementById('start-now');
var xmlhttp=new XMLHttpRequest();
var control = document.getElementById('control')


for (i=0;i<playlist.length;i++){
	playlist[i].addEventListener("click",select,false);
  playlist[i].getElementsByTagName('audio')[0].addEventListener("timeupdate", timeUpdate, false);
}

timeline.addEventListener("click", function (event) {
	moveplayhead(event);
	music.currentTime = music.duration * clickPercent(event);
}, false);

playhead.addEventListener('mousedown', mouseDown, false);
window.addEventListener('mouseup', mouseUp, false);
predict.addEventListener('click',process,false);

function showResponse(responseText, statusText)  {
    console.log(responseText);
		$('#control').append('<h2>Current track belongs to '+responseText+'</h2>')
}

var options = {
    success:       showResponse  // post-submit callback
};

function getSongs(files){
		if(document.getElementsByClassName('currentTrack')[0] !== undefined){
			document.getElementsByClassName('currentTrack')[0].className=('track');
			music.pause();
			pButton.className = "play";
			music.currentTime = 0;
		}
		fileName = files[0].name;
		control.innerHTML ='<h2>'+fileName+'</h2><a id="start-now"><h2>Tap to predict</h2></a>';
		$('#upload-text').remove();
		predict.removeEventListener('click',process,false);
		predict = document.getElementById('start-now');
		predict.addEventListener('click',process,false);
}

function process(){
	if(document.getElementById('upload-text') == null){
		$('form').ajaxSubmit(options);
	} else{
		var trackNum = document.getElementsByClassName('currentTrack')[0].id;
		$.post("process", trackNum, function(data){
		   console.log(data);
			 control.innerHTML ='<a id="start-now"><h2>Tap to predict</h2></a>';
			 $('#upload-text').remove();
			 $('#control').append('<h2>Current track belongs to '+data+'</h2>')
		 });
	}
}

function select(){
	if(document.getElementById('upload-text')==undefined){
		control.innerHTML ='<a id="start-now"><h2>Tap to predict</h2></a><h2>or</h2>'
		predict.removeEventListener('click',process,false);
		predict = document.getElementById('start-now');
		predict.addEventListener('click',process,false);
		$('form').append('<label id = "upload-text"for="file"><h2>Choose your own track...</h2></label>');
	}
	if (this.class !== "currentTrack"){
		temp = document.getElementsByClassName('currentTrack')[0];
		if (temp !== undefined){
			document.getElementsByClassName('currentTrack')[0].className=('track');
		}
		this.className="currentTrack";
    if (music !== undefined){
      music.pause();
    }
    music = this.getElementsByTagName('audio')[0];
    music.currentTime = 0;
    play();
	}
}

function play() {
  if (music == undefined){
    music = playlist[0].getElementsByTagName('audio')[0];
    playlist[0].className="currentTrack";
  }
	if (music.paused) {
		music.play();
		pButton.className = "";
		pButton.className = "pause";
	} else {
		music.pause();
		pButton.className = "";
		pButton.className = "play";
	}
}

function clickPercent(e) {
  console.log(e.pageX);
  console.log(timeline.offsetLeft-timeline.offsetParent.offsetLeft);
	return (e.pageX - timeline.offsetLeft-timeline.offsetParent.offsetLeft) / timelineWidth;
}

function mouseDown() {
	onplayhead = true;
	window.addEventListener('mousemove', moveplayhead, true);
	music.removeEventListener('timeupdate', timeUpdate, false);
}

function mouseUp(e) {
	if (onplayhead == true) {
		moveplayhead(e);
		window.removeEventListener('mousemove', moveplayhead, true);
		// change current time
		music.currentTime = music.duration * clickPercent(e);
		music.addEventListener('timeupdate', timeUpdate, false);
	}
	onplayhead = false;
}

function moveplayhead(e) {
	var newMargLeft = e.pageX - timeline.offsetLeft-timeline.offsetParent.offsetLeft;
	if (newMargLeft >= 0 && newMargLeft <= timelineWidth) {
		playhead.style.marginLeft = newMargLeft + "px";
	}
	if (newMargLeft < 0) {
		playhead.style.marginLeft = "0px";
	}
	if (newMargLeft > timelineWidth) {
		playhead.style.marginLeft = timelineWidth + "px";
	}
}

function timeUpdate() {
	var playPercent = timelineWidth * (music.currentTime / music.duration);
	playhead.style.marginLeft = playPercent + "px";
	if (music.currentTime == music.duration) {
		pButton.className = "";
		pButton.className = "play";
	}
}

//audio player end
