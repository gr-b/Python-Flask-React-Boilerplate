import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Home from './Home';

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
    errorElement: <p>error not found 404</p>
  },
  { 
    path: "/other_path",
    element: <p> This is another path </p>
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
