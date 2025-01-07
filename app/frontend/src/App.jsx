import React, { useState, useEffect } from 'react';

function App() {
  const [message, setMessage] = useState('');
  const [selectedFile, setSelectedFile] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [annotatedImage, setAnnotatedImage] = useState(null);

  // Fetch message from the backend on load
  useEffect(() => {
    fetch('http://127.0.0.1:5001/')
      .then((response) => response.json())
      .then((data) => setMessage(data.message))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!selectedFile) {
      alert('Please select a file first!');
      return;
    }

    const formData = new FormData();
    formData.append('image', selectedFile);

    setLoading(true);
    setError('');
    setPrediction(null); // Reset prediction state
    setAnnotatedImage(null); // Reset annotated image state

    try {
      const response = await fetch('http://127.0.0.1:5001/predict', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'An unknown error occurred.');
      }

      const blob = await response.blob(); // Le backend retourne une image blob
      const imageUrl = URL.createObjectURL(blob); // Convertir le blob en URL utilisable
      setAnnotatedImage(imageUrl); // Mettre à jour l'état avec l'URL de l'image annotée
    } catch (error) {
      console.error('Error during prediction:', error);
      setError(error.message || 'Something went wrong. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Waste Recognition Application</h1>
      <p>{message}</p>

      <p>This application allows you to identify the type of waste in a photo you upload. Simply select an image and click "Upload and Predict" to get started.</p>

      <form onSubmit={handleSubmit} style={{ marginTop: '20px' }}>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <button type="submit">Upload and Predict</button>
      </form>

      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {annotatedImage && (
        <div>
          <h2>Annotated Image:</h2>
          <img
            src={annotatedImage}
            alt="Annotated Prediction"
            style={{ maxWidth: '100%', marginTop: '20px', border: '2px solid #ccc' }}
          />
        </div>
      )}
    </div>
  );
}

export default App;
