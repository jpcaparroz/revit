"use client";

import Image from "next/image";
import Link from "next/link";
import { useEffect, useState } from "react";
import { themeObject } from "@/app/context/theme";
import { useTheme } from "@/app/context/ThemeContext";
import { Toggle } from "@/app/components/toggle/themeToggle";
import "./page.css";

const Revit = () => {
    const [fileName, setFileName] = useState<string | null>(null);
    const [fileContent, setFileContent] = useState<string | null>(null);
    const [fileCharsCount, setFileCharsCount] = useState<number | null>(null);
    const [fileChunksCount, setFileChunksCount] = useState<number | null>(null);
    const [summary, setSummary] = useState<string | null>(null);
    const [summarizeDuration, setSummarizeDuration] = useState<string | null>(null);
    const [summarizeCharCount, setSummarizeCount] = useState<number | null>(null);
    const [reviteSummary, setRevitSummary] = useState<string | null>(null);

    const { theme } = useTheme();

    useEffect(() => {
        const urlParams = new URLSearchParams(window.location.search);
        const fileNameParam = urlParams.get("file_name");
        const fileContentParam = urlParams.get("file_content");
        const fileCharsCountParam = urlParams.get("file_chars_count");
        const fileChunksCountParam = urlParams.get("file_chunks_count");
        const summaryParam = urlParams.get("summary");
        const summarizeDurationParam = urlParams.get("summarize_duration");
        const summarizeCharsCountParam = urlParams.get("summarize_chars_count");
        const revitSummaryParam = urlParams.get("revit_summary_message");

        setFileName(fileNameParam);
        setFileContent(fileContentParam);
        setFileCharsCount(Number(fileCharsCountParam));
        setFileChunksCount(Number(fileChunksCountParam));
        setSummary(summaryParam);
        setSummarizeDuration(summarizeDurationParam);
        setSummarizeCount(Number(summarizeCharsCountParam));
        setRevitSummary(revitSummaryParam);

    }, []);

    return (
        <div
            className="home"
            style={{
                background: themeObject[theme].background,
                transition: "background 0.5s ease-in-out, color 0.5s ease-in-out",
            }}
        >
            <Toggle />

            <Link href="/" className="logo">
                <Image
                    src={themeObject[theme].image}
                    alt="Logo da Loopdevs"
                    width={100}
                    height={100}
                />
            </Link>

            <div className="revit-box" style={{background: themeObject[theme].boxColor, color: themeObject[theme].boxFontColor}}>
                {summary ? (
                    <div>
                        Olá, eu sou o Revit! Construído pela Loopdevs para resumir seus PDFs.
                        <br />
                        Abaixo está o resumo do seu arquivo <strong>{fileName}</strong> =)

                        <br />
                        <br />
                        <strong>Resumo:</strong>
                        <br />
                        {summary}

                        <br />
                        <br />
                        <strong>Detalhes:</strong>
                        <br />
                        <strong>Nome do Arquivo:</strong> {fileName}
                        <br />
                        <strong>Quantidade de Caracteres de Origem:</strong> {fileCharsCount}
                        <br />
                        <strong>Quantidade de Chunks para o Resumo:</strong> {fileChunksCount}
                        <br />
                        <strong>Duração da Criação do Resumo:</strong> {summarizeDuration}
                        <br />
                        <strong>Quantidade de Caracteres do Resumo:</strong> {summarizeCharCount}
                    </div>
                ) : (
                    <p>Carregando conteúdo...</p>
                )}
            </div>
        </div>
    );
};

export default Revit;
