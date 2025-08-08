import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import IntroPage from "./pages/IntroPage";
import UploadPage from "./pages/UploadPage";
import VisualizationPage from "./pages/VisualizationPage";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<IntroPage />} />
        <Route path="/upload" element={<UploadPage />} />
        <Route path="/visualize/:jobId" element={<VisualizationPage />} />
      </Routes>
    </Router>
  );
}
