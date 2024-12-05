"use client";

import "./themeToggle.css";
import { useTheme } from "@/app/context/ThemeContext";

export function Toggle() {
    const { theme, toggleTheme } = useTheme();

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        toggleTheme();
    };

    return (
        <label className="switch">
            <input
                type="checkbox"
                checked={theme === "light"}
                onChange={handleChange}
            />
            <span className="slider round"></span>
        </label>
    );
}
