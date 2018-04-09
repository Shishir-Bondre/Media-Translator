function setRadioBoxValue(e){
        var recordedAudio=document.querySelector('input[name="recordedAudio"]:checked').value
        console.log(recordedAudio);
        var setRecordingValue = document.getElementById('uploadRecording');
        setRecordingValue.href=recordedAudio;
        // showMediaPlayer(recordedAudio);
}
// function showMediaPlayer(recordedAudio){
//         if(recordedAudio == 1)
//         {
//                 recordedAudio = document.getElementsByClassName('audioFile').value;
//         }
//         console.log("this is showMediaPlayer");
//         document.getElementById('mainPlayer').style.display="block";
//         var sound=document.getElementById('mainSound');
//         sound.src = recordedAudio;
// }