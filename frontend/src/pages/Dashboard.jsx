import React, { useState } from "react";
import FileUploader from "../components/FileUploader";
import ModelSelector from "../components/ModelSelector";
import SummaryViewer from "../components/SummaryViewer";
import { summarizeDocument } from "../services/api";

const Dashboard = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [selectedModel, setSelectedModel] = useState("openai-gpt-4");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const availableModels = [
    "openai-gpt-4",
    "mistral-7b",
    "llama-2-13b",
    "gemini-1.0",
  ];

  const handleSummarize = async () => {
    if (!selectedFile) {
      setError("Please select a file.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const formData = new FormData();
      formData.append("file", selectedFile);
      formData.append("model", selectedModel);

      const res = await summarizeDocument(formData);
      setSummary(res.data.summary);
    } catch (err) {
      setError("Error while summarizing.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <header className="bg-white shadow-md p-4">
        <h1 className="text-xl font-bold text-gray-800">
          🛰️ Intelligence Summarizer
        </h1>
      </header>

      <main className="flex flex-col md:flex-row gap-4 p-6 flex-1">
        {/* Left Section */}
        <div className="md:w-1/3 bg-white shadow-md rounded-lg p-4">
          <FileUploader onFileSelect={setSelectedFile} />
          <ModelSelector
            models={availableModels}
            selectedModel={selectedModel}
            onChange={setSelectedModel}
          />
          <button
            onClick={handleSummarize}
            disabled={loading}
            className="w-full bg-blue-600 text-white py-2 rounded-lg mt-4 hover:bg-blue-700"
          >
            {loading ? "Summarizing..." : "Summarize"}
          </button>
          {error && <p className="text-red-500 mt-3">{error}</p>}
        </div>

        {/* Right Section */}
        <div className="md:w-2/3 bg-white shadow-md rounded-lg p-4">
          <SummaryViewer summary={summary} />
        </div>
      </main>
    </div>
  );
};

export default Dashboard;
