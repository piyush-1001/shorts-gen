
// var socket = io();

// socket.on('progress_update', function(data) {
//     document.getElementById("t2").value = data.progress;
// });

// function generate() {
//     var text = document.getElementById("t1").value;
//     socket.emit('process_text', {text: text});
// }


// function generate() {
//     var text = document.getElementById("t1").value;
//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", "/process_text", true);
//     xhr.setRequestHeader("Content-Type", "application/json");
//     xhr.onreadystatechange = function () {
//         if (xhr.readyState === 4 && xhr.status === 200) {
//             // document.getElementById("t2").value = "VIDEO GENERATED YAY!!";
//         }
//     };
//     xhr.send(JSON.stringify({ text: text }));


//     var source = new EventSource("/process_text");
//     source.onmessage = function(event) {
//         var update = JSON.parse(event.data);
//         if (update.type === 'progress') {
//             document.getElementById("t2").value = update.message;
//             // You can also use update.step to show progress percentage, for example
//         } else {
//             // Handle other types of messages if needed
//         }
//     };

// }



function generate() {
    var text = document.getElementById('t1').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/process_text', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 3 && xhr.status === 200) {
            var responseData = xhr.responseText;
            document.getElementById('t2').value = responseData;
        }
    };
    xhr.send(JSON.stringify({ 'text': text }));
}
