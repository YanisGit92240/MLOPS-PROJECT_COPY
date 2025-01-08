import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders frontend message', () => {
  render(<App />);
  const headerElement = screen.getByText(/Waste Recognition Application/i);
  expect(headerElement).toBeInTheDocument();
});

test('renders the Upload and Predict button', () => {
  render(<App />);
  const buttonElement = screen.getByRole('button', { name: /Upload and Predict/i });
  expect(buttonElement).toBeInTheDocument();
  expect(buttonElement).toBeEnabled();
});

test('displays loading message while processing prediction', async () => {
  render(<App />);

  // Simulez une sélection de fichier
  const fileInput = screen.getByLabelText(/Choose File/i) || screen.getByRole('button', { name: /Choose File/i });
  const file = new File(['dummy-content'], 'example.png', { type: 'image/png' });
  Object.defineProperty(fileInput, 'files', {
    value: [file],
  });

  fireEvent.change(fileInput);

  // Simulez un clic sur le bouton "Upload and Predict"
  const buttonElement = screen.getByText(/Upload and Predict/i);
  fireEvent.click(buttonElement);

  // Vérifiez si le message de chargement apparaît
  const loadingMessage = await waitFor(() => screen.getByText(/Loading.../i));
  expect(loadingMessage).toBeInTheDocument();
});
