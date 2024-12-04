"use client";

import React from "react";
import { themeObject } from "@/app/context/theme";
import { useTheme } from "@/app/context/ThemeContext";

const LoadingSpinner = () => {
    const { theme } = useTheme();

    return (
        <div
            className="loading-container"
            style={{
                // background: themeObject[theme].background,
                color: themeObject[theme].color,
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: "100vh",
                flexDirection: "column",
                transition: "background 0.5s ease-in-out, color 0.5s ease-in-out",
            }}
        >
            <div className="spinner" style={{ marginBottom: "20px" }}>
            </div>
            <p style={{ fontSize: "18px" }}>Carregando...</p>

            <style jsx>{`
                .spinner {
                    display: inline-block;
                    width: 100px;
                    height: 100px;
                    border-radius: 50%;
                    border: 10px solid ${themeObject[theme].loadingColorBase};
                    border-top: 10px solid ${themeObject[theme].loadingColor};
                    animation: spin 2s linear infinite;
                }

                @keyframes spin {
                    0% {
                        transform: rotate(0deg);
                    }
                    100% {
                        transform: rotate(360deg);
                    }
                }
            `}</style>
        </div>
    );
};

export default LoadingSpinner;
