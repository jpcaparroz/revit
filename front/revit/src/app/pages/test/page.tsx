"use client";

import React, { useState } from "react";
import axios from "axios";

const Upload = () => {
    const [file, setFile] = useState<File | null>(null);
    const [response, setResponse] = useState<string | null>(null);
    const [error, setError] = useState<string | null>(null);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files[0]) {
            setFile(event.target.files[0]);
            setResponse(null);
            setError(null);
        }
    };

    const handleUpload = async () => {
        if (!file) {
            alert("Por favor, selecione um arquivo.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {
            const res = await axios.post("http://localhost:8080/api/v1/revit/read_pdf/", formData, {
                headers: { "Content-Type": "multipart/form-data" },
            });

            console.log(res.data.detail);
            
            setResponse(res.data.detail);
            setError(null);
        } catch (err) {
            setError("Erro ao enviar o arquivo!");
        }
    };

    return (
        <div>
            <h1>Upload de PDF</h1>
            <input type="file" accept=".pdf" onChange={handleFileChange} />
            <button onClick={handleUpload}>Enviar</button>

            {error && <p style={{ color: "red" }}>{error}</p>}

            {response && (
                <div>
                    <h2>Conteúdo do PDF:</h2>
                    <pre>{response}</pre>
                </div>
            )}
        </div>
    );
};

export default Upload;
