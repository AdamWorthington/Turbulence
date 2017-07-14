while true
do
sleep 1
printf "Turbine $1 status: "
sudo curl -H "Accept: application/json" "https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/$1/heartbeat"
printf "\nTemp Turbine $1: "
sudo curl -H "Accept: application/json" "https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/$1/sensors/temperature"
printf "\nVoltage Turbine $1: "
sudo curl -H "Accept: application/json" "https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/$1/sensors/voltage"
printf "\n\n"
done