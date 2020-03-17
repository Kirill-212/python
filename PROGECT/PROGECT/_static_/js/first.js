function zero_first_format(value)
    {
        if (value < 10)
        {
            value='0'+value;
        }
        return value;
    }

    /* функция получения текущей даты и времени */
    function date_time()
    {
        var current_datetime = new Date();
        var hours = zero_first_format(current_datetime.getHours());
        var minutes = zero_first_format(current_datetime.getMinutes());
        var seconds = zero_first_format(current_datetime.getSeconds());

        return " "+hours+":"+minutes+":"+seconds;
    }
    setInterval(function () {
        document.getElementById('_time').innerHTML = date_time();
    }, 1000);





var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [0, 10, 5, 2, 20, 30, 45]
        }]
    },

    options: {}
});

