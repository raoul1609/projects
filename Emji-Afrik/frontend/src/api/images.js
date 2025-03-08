import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/creations/';  // Remplacez par l'URL de votre backend Django

export const getImages = async () => {
    const response = await axios.get(`${API_URL}/images/`);
    return response.data;
};

export const uploadImage = async (file, title, description) => {
    const formData = new FormData();
    formData.append('image', file);
    formData.append('title', title);
    formData.append('description', description);

    const response = await axios.post(`${API_URL}/images/`, formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
    return response.data;
};

export const deleteImage = async (id) => {
    await axios.delete(`${API_URL}/images/${id}/`);
};