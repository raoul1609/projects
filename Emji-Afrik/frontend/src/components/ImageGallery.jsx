import React, { useEffect, useState } from 'react';
import { getImages, deleteImage } from '../api/images';

const ImageGallery = () => {
    const [images, setImages] = useState([]);

    useEffect(() => {
        const fetchImages = async () => {
            const data = await getImages();
            setImages(data);
        };
        fetchImages();
    }, []);

    const handleDelete = async (id) => {
        await deleteImage(id);
        setImages(images.filter(image => image.id !== id));
    };

    return (
        <div>
            <h1>Galerie d'images</h1>
            <div style={{ display: 'flex', flexWrap: 'wrap' }}>
                {images.map(image => (
                    <div key={image.id} style={{ margin: '10px', textAlign: 'center' }}>
                        <img
                            //src={`http://127.0.0.1:8000${image.image}`}
                            src={image.image}
                            alt={image.title}
                            style={{ maxWidth: '200px', axHeight: '200px' }}
                        />
                        <h3>{image.title}</h3>
                        <p>{image.description}</p>
                        <p>{image.prix} FCFA </p>
                        <p><strong>{image.categorie}</strong></p>
                        <button onClick={() => handleDelete(image.id)}>Supprimer</button>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ImageGallery;