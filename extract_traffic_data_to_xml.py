import xml.etree.ElementTree as ET

def parse_traces(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    traces = {}
    for vehicle in root.findall('vehicle'):
        vid = vehicle.get('id')
        route = vehicle.find('route').text
        traces[vid] = route.split()
    return traces

if __name__ == "__main__":
    traces = parse_traces('yourTrips.trips.xml')
    for vid, route in traces.items():
        print(f"Vehicle {vid}: {route}")

