function handleClick(event)
{
    var clickedButton = event.target;

    if (clickedButton.id === 'btOn')
    {
        var data = {
            onoff: 1
        };
    }
    else
    {
        var data = {
            onoff: 0
        };
    }
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };
    
    fetch(newUrl, options)
        .then(response => response.json())
        .then(result => {
            console.log('Response:', result);
            // Handle the response data
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle any errors
        });
}

var route = 'toggle';
var baseUrlFromFlask = document.getElementById('baseUrlFromFlask').dataset.url;
var portFromFlask = document.getElementById('portFromFlask').dataset.port;
var newUrl = new URL(route,baseUrlFromFlask);
newUrl.port = portFromFlask;

console.log(newUrl.href);

document.addEventListener('DOMContentLoaded', () => {
    const buttonon = document.getElementById('btOn');
    const buttonoff = document.getElementById('btOff');
    buttonon.addEventListener('click', handleClick);
    buttonoff.addEventListener('click', handleClick);
    console.log("Event listerners registred!");      
});

console.log("Script loaded!")
