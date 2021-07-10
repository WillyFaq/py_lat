document.addEventListener('DOMContentLoaded', function(event) {
    // Initialize everything and start rendering

    //video.src = 'http://192.168.1.16:4747/mjpegfeed';
    /*var a = window.URL.createObjectURL('http://192.168.1.16:4747');
    console.log(a);*/
    /*var constrains = {
        video: {
            mandatory: {
                minWidth: window.innerWidth,
            }
        }
    };

    if (navigator.mediaDevices.getUserMedia) {
        console.log("getusasd");
        navigator.mediaDevices.getUserMedia({}, function(stream) {
            console.log("meda");
            video.src = window.URL.createObjectURL(stream);

            video.oncanplay = function() {
               
            }

        }, function() {});
    }*/

    /*if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
        })
        .catch(function (err0r) {
            console.log("Something went wrong!");
        });
    }*/
});