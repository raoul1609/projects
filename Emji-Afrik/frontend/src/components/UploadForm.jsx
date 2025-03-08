import React, { useState } from 'react';
import { uploadImage } from '../api/images';

const UploadForm = ({ onUpload }) => {
    const [file, setFile] = useState(null);
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        await uploadImage(file, title, description);
        alert('Image téléversée avec succès !');
        onUpload();  // Rafraîchir la galerie après le téléversement
        setFile(null);
        setTitle('');
        setDescription('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Téléverser une image</h2>
            <input
                type="file"
                onChange={(e) => setFile(e.target.files[0])}
                required
            />
            <input
                type="text"
                placeholder="Titre"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                required
            />
            <textarea
                placeholder="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />
            <button type="submit">Téléverser</button>
        </form>
    );
};

export default UploadForm;