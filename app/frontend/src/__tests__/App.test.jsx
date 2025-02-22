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

