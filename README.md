# IoT Temperature Monitoring - MQTT to Grafana

Proyek ini bertujuan untuk memonitor suhu secara real-time dari sensor IoT yang dikirim melalui protokol MQTT, dikumpulkan oleh Telegraf, disimpan di InfluxDB, dan divisualisasikan menggunakan Grafana.


## Komponen yang Digunakan
- Python (`paho-mqtt`) sebagai publisher
- HiveMQ sebagai MQTT Broker
- Telegraf sebagai data collector
- InfluxDB v1.8 sebagai database time-series
- Grafana sebagai visualisasi dashboard

## Struktur Project
iot_mqtt_project/
├── publisher.py
├── subscriber.py
├── docker-compose.yml
├── telegraf.conf
└── README.md
