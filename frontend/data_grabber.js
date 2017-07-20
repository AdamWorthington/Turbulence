$(document).ready(function() {
    queryTurbines();
    setInterval("queryTurbines()",5000);
});

function queryTurbines() { 
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
}



var settings = {
  "async": true,
  "crossDomain": true,
  "url": "https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints",
  "method": "POST",
  "headers": {
    "predix-zone-id": "d97f5953-2c07-4e8f-ac0d-8b8df897135e",
    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI3ODY1YzU2NmRiMWU0MmRjYTUwYWVlYzFlNTMzNjgyMiIsInN1YiI6InRzLWNsaWVudDEiLCJzY29wZSI6WyJ1YWEucmVzb3VyY2UiLCJ0aW1lc2VyaWVzLnpvbmVzLmQ5N2Y1OTUzLTJjMDctNGU4Zi1hYzBkLThiOGRmODk3MTM1ZS5pbmdlc3QiLCJ1YWEubm9uZSIsInRpbWVzZXJpZXMuem9uZXMuZDk3ZjU5NTMtMmMwNy00ZThmLWFjMGQtOGI4ZGY4OTcxMzVlLnVzZXIiLCJ0aW1lc2VyaWVzLnpvbmVzLmQ5N2Y1OTUzLTJjMDctNGU4Zi1hYzBkLThiOGRmODk3MTM1ZS5xdWVyeSJdLCJjbGllbnRfaWQiOiJ0cy1jbGllbnQxIiwiY2lkIjoidHMtY2xpZW50MSIsImF6cCI6InRzLWNsaWVudDEiLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjlkYWMxM2ZmIiwiaWF0IjoxNTAwNDg2NDUwLCJleHAiOjE1MDE1Mzc2NTAsImlzcyI6Imh0dHBzOi8vZmYyMzU5ZDYtMDViNC00YTBmLTkwMDEtMjUzM2M3N2NmZTlkLnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiZmYyMzU5ZDYtMDViNC00YTBmLTkwMDEtMjUzM2M3N2NmZTlkIiwiYXVkIjpbInRpbWVzZXJpZXMuem9uZXMuZDk3ZjU5NTMtMmMwNy00ZThmLWFjMGQtOGI4ZGY4OTcxMzVlIiwidWFhIiwidHMtY2xpZW50MSJdfQ.LmGAVlyMCZ32TSLuhMZla0wNAJJfV2AaBfah0JPCvcajGWs4Z_q2DJRL5oS_xtEziwgF7qe5xtkKPzW3Lb0pWHn95IrrvxQimF36Es381kGOvBVQcIiKWkQ_wMk1-zRll04HpeZtCURV3tvzudu1XOy71hqTgPWmK-OhFBWvLqdkLnN6kNAvHm9yG3vmIS9QI3BLuN6yJOH_rDRl3IN0MFQbbL7r6IpyNOY6bkQqw7fp8xnxv03UER6fqLlCV17iwNXFfsap0RVrRvcdELwnfgfhnbTdGB_dcAx68u9kdBoehqjavUl5mCV2B5leMI9q9Ef4loIjTyVFKkHBfFnNVQ",
    "cache-control": "no-cache",
    "postman-token": "d58009d4-c3fd-d365-7077-fc6fd62ef816"
  },
  "data": "{\r\n    \"start\": 0,\r\n    \"end\": 99999999999,\r\n    \"tags\": [\r\n        {\r\n        \"name\": \"turbulence-turbine-1-temperature\"\r\n        }\r\n    ]\r\n}"
}

 function getAll(){

   var formData = {};
    return $.ajax(settings).then(requestSuccess, requestFail);

 }

 function fetchAndDownload(){

   var formData = {};
    return $.ajax(settings).then(requestSuccess, requestFail);

 }

 function requestSuccess(response){

   return response.tags["0"].results["0"].values.map(function(item){
      var record = {};
      record.time = item[0];
      record.temp = item[1];
      record.volt = item[2];
      return record;
    });
  }

 function requestFail (jqXHR, textStatus){
    return { error : textStatus };
  }

  function exportToCsv(filename, rows) {
          var processRow = function (row) {
              var finalVal = '';
              for (var j = 0; j < row.length; j++) {
                  var innerValue = row[j] === null ? '' : row[j].toString();
                  if (row[j] instanceof Date) {
                      innerValue = row[j].toLocaleString();
                  };
                  var result = innerValue.replace(/"/g, '""');
                  if (result.search(/("|,|\n)/g) >= 0)
                      result = '"' + result + '"';
                  if (j > 0)
                      finalVal += ',';
                  finalVal += result;
              }
              return finalVal + '\n';
          };

          var csvFile = '';
          for (var i = 0; i < rows.length; i++) {
              csvFile += processRow(rows[i]);
          }

          var blob = new Blob([csvFile], { type: 'text/csv;charset=utf-8;' });
          if (navigator.msSaveBlob) { // IE 10+
              navigator.msSaveBlob(blob, filename);
          } else {
              var link = document.createElement("a");
              if (link.download !== undefined) { // feature detection
                  // Browsers that support HTML5 download attribute
                  var url = URL.createObjectURL(blob);
                  link.setAttribute("href", url);
                  link.setAttribute("download", filename);
                  link.style.visibility = 'hidden';
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
              }
          }
      }

 fetchAndDownload().done(function(res){
    var arrayLength = res.length;
    console.log(arrayLength);
    var timeArray = [];
    var tempArray = [];
    var voltArray = [];
    for (var i = 0; i < arrayLength; i++) {
        timeArray.push(res[i].time);
        tempArray.push(res[i].temp);
        voltArray.push(res[i].volt);
        console.log(timeArray)
    }
   exportToCsv('data.csv', [
    [timeArray],
    [tempArray],
    [voltArray]
    ])
   // console.log(res[0].time)
   // console.log(JSON.stringify(res));

 }).fail(function(err){

   console.log(err);
    
 });
