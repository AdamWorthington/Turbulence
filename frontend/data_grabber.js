$.ajax({
    url: 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/sensors/temperature',
    success: function(data) {
        data_string = JSON.stringify(data)
        $('#turbine1').html(data_string);
        $('#turbine1-container').removeClass("red-jumbotron")
        console.log("success: " + data_string)
    },
    error: function(error) {
        console.log("error: " + error)
        error = "There is no data to display. Turbine 1 is down."
        $('#turbine1').html(error);
        $('#turbine1-container').addClass("red-jumbotron")
    }
});
$.ajax({
    url: 'http://echo.jsontest.com/key/value/one/two',
    dataType: 'jsonp',
    success: function(data) {
        data_string = JSON.stringify(data)
        $('#turbine2').html(data_string);
        $('#turbine2-container').removeClass("red-jumbotron")
        console.log("success for jsonp to json: " + data_string)

    },
    error: function(error) {
        console.log("error: " + error)
        error = "There is no data to display. Turbine 2 is down."
        $('#turbine2').html(error);
        $('#turbine2-container').addClass("red-jumbotron")

    }
});
$.ajax({
    url: 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/sensors/temperature',
    success: function(data) {
        data_string = JSON.stringify(data)
        $('#turbine3').html(data_string);
        $('#turbine3-container').removeClass("red-jumbotron")
        console.log("success: " + data_string)

    },
    error: function(error) {
        console.log("error: " + error)
        error = "There is no data to display. Turbine 3 is down."
        $('#turbine3').html(error);
        $('#turbine3-container').addClass("red-jumbotron")

    }
});

$.getJSON("http://echo.jsontest.com/key/value/one/two", function(json) {
    console.log("json data from jsontest.com: " + json);
});