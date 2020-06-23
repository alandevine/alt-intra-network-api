export default async function getDevice(deviceID) {
    try {
        const response = await fetch({
            method: 'GET',
            url: `/api/devices/${deviceID}`
        });
        return response.devices;
    } catch(e) {
        return [];
    }
}