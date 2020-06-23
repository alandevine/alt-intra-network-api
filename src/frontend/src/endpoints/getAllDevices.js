export default async function getAllDevices() {
    try {
        const response = await fetch({
            method: 'GET',
            url: '/api/devices',
        });
        return response.devices;
    } catch(e) {
        return [];
    }
}