"use client";

import Image from "next/image";
import Link from "next/link";
import "./page.css";
import { Toggle } from "@/app/components/toggle/themeToggle";
import { useEffect, useState } from "react";
import { themeObject } from "@/app/context/theme";
import { useTheme } from "@/app/context/ThemeContext";

export default function HomePage() {
    const [isMounted, setIsMounted] = useState(false);
    const { theme } = useTheme();

    useEffect(() => {
        setIsMounted(true);
    }, []);

    if (!isMounted) return null;

    return (
        <div
            className={`home ${theme}`}
            style={{
                background: themeObject[theme].background,
                color: themeObject[theme].color,
                transition:
                    "background 0.5s ease-in-out, color 0.5s ease-in-out",
            }}
        >
            <Toggle />

            <div className="title-box">
                <h1
                    className="title"
                    style={{ color: themeObject[theme].color }}
                >
                    REVIT
                </h1>
                <p className="sub-title">loopdevs documents ai</p>
            </div>

            <div className="continue-box">
                <Link href="/pages/revit-upload">
                    <Image
                        src={themeObject[theme].image}
                        className="logo"
                        alt="Loopdevs logo"
                        width={150}
                        height={150}
                        priority
                    />
                </Link>

                <Link href={"/pages/revit-upload"} className="continue">
                    click to continue
                </Link>
            </div>
        </div>
    );
}
