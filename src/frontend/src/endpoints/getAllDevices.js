export default async function getAllDevices() {
    try {
        const response = await fetch(`/api/devices`, {
            method: 'GET'
        });
        console.log(response)
        return response.devices;
    } catch(e) {
        return [];
    }
}