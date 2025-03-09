import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/creations/';  // Remplacez par l'URL de votre backend Django

export const getImages = async () => {
    const response = await axios.get(`${API_URL}`);
    return response.data;
};

export const uploadImage = async (file, title, description, prix) => {
    const formData = new FormData();
    formData.append('image', file);
    formData.append('titre', title);
    formData.append('prix', prix);
    formData.append('description', description);

    const response = await axios.post(`${API_URL}`, formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
    return response.data;
};

export const deleteImage = async (id) => {
    await axios.delete(`${API_URL}${id}/`);
};