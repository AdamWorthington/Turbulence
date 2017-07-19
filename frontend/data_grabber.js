$.ajax({
    url: 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/sensors/temperature',
    success: function(data) {
        // data_string = JSON.stringify(data)
        data_string = "Turbine 1 is up!"
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
    url: 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/temperature',
        success: function(data) {
        // data_string = JSON.stringify(data)
        data_string = "Turbine 2 is up!"
        $('#turbine2').html(data_string);
        $('#turbine2-container').removeClass("red-jumbotron")
        console.log("success: " + data_string)

    },
    error: function(error) {
        console.log("error: " + error)
        error = "There is no data to display. Turbine 2 is currently down."
        $('#turbine2').html(error);
        $('#turbine2-container').addClass("red-jumbotron")

    }
});
$.ajax({
    url: 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/sensors/temperature',
    success: function(data) {
        // data_string = JSON.stringify(data)
        data_string = "Turbine 3 is up!"
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