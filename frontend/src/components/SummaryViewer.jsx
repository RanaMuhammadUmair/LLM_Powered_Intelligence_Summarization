import React from "react";

const SummaryViewer = ({ summary }) => {
  return (
    <div>
      <h2 className="text-lg font-semibold mb-3 text-gray-700">
        Generated Summary:
      </h2>
      <div className="bg-gray-50 p-4 rounded-lg border border-gray-200 min-h-[200px] whitespace-pre-line">
        {summary || "No summary yet."}
      </div>
    </div>
  );
};

export default SummaryViewer;
