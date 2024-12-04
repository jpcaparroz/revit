"use client";

import axios from "axios";
import Image from "next/image";
import Link from "next/link";
import { Toggle } from "@/app/components/toggle/themeToggle";
import { useState } from "react";
import { themeObject } from "@/app/context/theme";
import { useTheme } from "@/app/context/ThemeContext";
import { useRouter } from "next/navigation";
import LoadingSpinner from "@/app/components/loading/loading"; // Importe o componente de carregamento
import "./page.css";

const Upload = () => {
    const [error, setError] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState<boolean>(false); // Estado para controlar o carregamento
    const { theme } = useTheme();
    const router = useRouter();

    const handleFileChange = async (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files[0]) {
            const file = event.target.files[0];

            const formData = new FormData();
            formData.append("file", file);

            setIsLoading(true); // Começa o carregamento

            try {
                const res = await axios.post("http://localhost:8080/api/v1/revit/", formData, {
                    headers: { "Content-Type": "multipart/form-data" },
                });

                const {
                    file_name,
                    file_content,
                    file_chars_count,
                    file_chunks_count,
                    summary,
                    summarize_duration,
                    summarize_chars_count,
                    revit_summary_message
                } = res.data;

                const params = new URLSearchParams({
                    file_name: file_name,
                    file_content: file_content,
                    file_chars_count: String(file_chars_count),
                    file_chunks_count: String(file_chunks_count),
                    summary: summary,
                    summarize_duration: summarize_duration,
                    summarize_chars_count: String(summarize_chars_count),
                    revit_summary_message: revit_summary_message
                });

                router.replace(`/pages/revit?${params.toString()}`);
                setError(null);
            } catch (err) {
                setError("Erro ao enviar o arquivo!");
                console.error(err);
            } finally {
                setIsLoading(false); // Finaliza o carregamento
            }
        }
    };

    return (
        <div
            className="home"
            style={{
                background: themeObject[theme].background,
                color: themeObject[theme].color,
                transition: "background 0.5s ease-in-out, color 0.5s ease-in-out",
            }}
        >
            <Toggle />

            <Link href="/" className="logo">
                <Image
                    src={themeObject[theme].image}
                    alt="Loopdevs logo"
                    width={100}
                    height={100}
                />
            </Link>

            {!isLoading && (
                <div className="upload-box">
                    <input
                        type="file"
                        id="file-upload"
                        accept=".pdf"
                        onChange={handleFileChange}
                        style={{ display: "none" }}
                    />
                    <label htmlFor="file-upload" className="upload-button">
                        <p className="upload-text">
                            upload your
                            <span style={{ fontWeight: "bold" }}> pdf</span> file
                        </p>
                        <Image
                            src={themeObject[theme].image2}
                            className="upload"
                            alt="Upload icon"
                            width={80}
                            height={80}
                        />
                    </label>
                </div>
            )

            }

            {isLoading && <LoadingSpinner />}

            {error && <p style={{ color: "red" }}>{error}</p>}
        </div>
    );
};

export default Upload;
