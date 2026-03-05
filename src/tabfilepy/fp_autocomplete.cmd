@REM tabfilepy; A simple Python library (with associated cmd/bash script) which allows file directory tab auto-completions. 
@REM This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.
@REM This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.
@REM You should have received a copy of the GNU Lesser General Public License along with this library; if not, see <https://www.gnu.org/licenses/>.

@ECHO OFF
setlocal EnableDelayedExpansion

REM Use provided argument as prompt, or default
set "prompt=%~1"

REM Ask for file path with custom prompt
set /p "filename=%prompt%"

REM Print out file path
ECHO !filename!

endlocal
