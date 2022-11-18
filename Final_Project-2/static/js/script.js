import location from '../data/location.json' assert {type: 'json'};

const selectForLocation = document.getElementById('location');
const radioButtons = document.querySelectorAll('input[type="radio"]');

document.addEventListener('DOMContentLoaded', function () {
    radioButtons[0].checked = true;
    let locationArr = location.sort((a, b) => a[1] - b[1]);
    for(let i = 0; i < location.length; i++) {
        let option = document.createElement("option");
        option.setAttribute('value', locationArr[i][1]);
        option.appendChild(document.createTextNode(locationArr[i][0]));
        selectForLocation.appendChild(option);
    }
})