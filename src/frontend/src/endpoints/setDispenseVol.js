export default async function setDispenseVol(deviceID, volume) {
    try {
        const response = await fetch(`api/devices/dispense_vol/${deviceID}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
              },
            body: volume
        });
        return response.json();
    } catch(e) {
        return "Error"
    }
}