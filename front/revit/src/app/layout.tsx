import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { ThemeProvider } from "./context/ThemeContext";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
    title: "Revit",
    description: "Revit",
};

export default function RootLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <html lang="pt-BR">
            <body className={inter.className}>
                <ThemeProvider>{children}</ThemeProvider>
            </body>
        </html>
    );
}
