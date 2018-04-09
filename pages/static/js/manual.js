function getRecording(){
    var recordedAudio=document.querySelector('input[name="rate"]:checked').value
    // document.getElementById("recording").value = recordedAudio;
    document.getElementById("recording").setAttribute('value',recordedAudio);
    console.log(recordedAudio);
    // console.log(document.getElementById("recording").value);
}
function getAudioFile(){
    var getAudioFile=document.getElementById('sound').src;
    //document.getElementById("fileInput").setAttribute('value',getAudioFile);
     document.getElementById("fileInput").value = getAudioFile;
    console.log(getAudioFile);
    // console.log(document.getElementById("fileInput").value);
}