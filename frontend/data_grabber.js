$.ajax({
  url: 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/sensors/temperature',
  dataType: 'jsonp',
  success: function(data) {
  $('#turbine1').html(data);
  $('#turbine1-container').removeClass("red-jumbotron")
  },
  error: function(e) {
        data = "There is no data to display. Turbine 1 is down."
        $('#turbine1').html(data);
        $('#turbine1-container').addClass("red-jumbotron")
  }
});
$.ajax({
  url: 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/temperature',
  dataType: 'jsonp',
  success: function(data) {
  $('#turbine2').html(data);
    $('#turbine2-container').removeClass("red-jumbotron")

  },
  error: function(e) {
        data = "There is no data to display. Turbine 2 is down."
        $('#turbine2').html(data);
        $('#turbine2-container').addClass("red-jumbotron")

  }
});
$.ajax({
  url: 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/sensors/temperature',
  dataType: 'jsonp',
  success: function(data) {
  $('#turbine3').html(data);
    $('#turbine3-container').removeClass("red-jumbotron")

  },
  error: function(e) {
        data = "There is no data to display. Turbine 3 is down."
        $('#turbine3').html(data);
        $('#turbine3-container').addClass("red-jumbotron")

  }
});