document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#form').onsubmit = () => {
        const request = new XMLHttpRequest();
        const currency = document.querySelector('#currency').value;
        request.open('POST', '/convert');
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            if (data.success) {
                const contents = `1 EURO is equal to ${data.rate} ${currency}.`
                document.querySelector('#result').innerHTML = contents;
            }
            else {
                document.querySelector('#result').innerHTML = 'There was an error.';
            }
        }
        const data = new FormData();
        data.append('currency', currency);
        request.send(data);
        return false;
    };

});
