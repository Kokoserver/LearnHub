
var videoPlayer = document.getElementById('videoPlayer')
var player = videojs(videoPlayer, {
    aspectRatio :"640:267",
    playbackRates: [0.25, 0.5 , 1, 1.5, 2, 2.5, 3, 3.5, 4],
    width:"640px" ,
    height:"267px",
    controls:true,
    preload: "auto",
    plugins:{
        hotkeys:{
            volumeStep: 0.1,
            seekStep: 5,
            enableModifiersForNumbers: false
        },
        
    }

})

var poster = player.getAttribute('poster')
var videoPlayer = document.getElementById('videoPlayer');
var video = document.getElementsByClassName("video-title")
var url = ()=>{
  var urls = document.getElementById('urls')
  return urls
}
var videoList = []
   for(var i =0; i<video.length; i++){
    var videos = video[i]
    var url = document.getElementsByClassName('url')
    videoList.push({
        sources: [{
            src: url[i].getAttribute('id'), 
            type: 'video/mp4',
            name: url[i].textContent
        }],  
      
        poster:poster
        })
    
   }

   var titleUpdater = ()=> { 
    var title =   document.getElementById('title-text').innerHTML =  player.cache_.source.name.replace('.mp4', ' ')
    }

player.on('play', function () {
    // console.log(this.currentSrc());
    // var name = player.playlist.indexOf(this.currentSrc())
    titleUpdater()
    
    
});
  function loadVideo(name ,element){
    document.getElementById('title-text').innerHTML = name
    player.src(element)
  player.play()
  
}


   
/* ADD PREVIOUS */
var Button = videojs.getComponent('Button');

// Extend default
var PrevButton = videojs.extend(Button, {
  //constructor: function(player, options) {
  constructor: function() {
    Button.apply(this, arguments);
    //this.addClass('vjs-chapters-button');
    this.addClass('icon-angle-left');
    this.controlText("Previous");
  },

  // constructor: function() {
  //   Button.apply(this, arguments);
  //   this.addClass('vjs-play-control vjs-control vjs-button vjs-paused');
  // },

  // createEl: function() {
  //   return Button.prototype.createEl('button', {
  //     //className: 'vjs-next-button vjs-control vjs-button',
  //     //innerHTML: 'Next >'
  //   });
  // },

  handleClick: function() {
    player.playlist.previous();
  }
});

/* ADD BUTTON */
var Button = videojs.getComponent('Button');

// Extend default
var NextButton = videojs.extend(Button, {
  //constructor: function(player, options) {
  constructor: function() {
    Button.apply(this, arguments);
    //this.addClass('vjs-chapters-button');
    this.addClass('icon-angle-right');
    this.controlText("Next");
  },

  handleClick: function() {
    // console.log('click');
    player.playlist.next();
  }
});

// Register the new component
videojs.registerComponent('NextButton', NextButton);
videojs.registerComponent('PrevButton', PrevButton);
player.getChild('controlBar').addChild('PrevButton', {}, 0);
player.getChild('controlBar').addChild('NextButton', {}, 2);







  player.playlist(videoList)
  player.playlist.autoadvance(0); // play all
