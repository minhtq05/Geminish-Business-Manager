import React from "react";
import { cn } from "@/lib/utils";
interface LogoProps{
    className?:string;
    logoImg: React.ReactNode;
    logoText?: string;
}

const Logo: React.FC<LogoProps> = ({logoImg, className, logoText} : LogoProps) => {
    return(
        <div className={cn("text-5xl text-indigo-500 flex flex-row items-center gap-2", className)}>
        {logoImg}
        <span className="text-4xl font-bold tracking-wide">{logoText}</span>
      </div>
    )
}
export default Logo;
